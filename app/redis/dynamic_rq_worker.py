import multiprocessing
import time

from rq import Connection, Worker

from app import redis_q, app


class DynamicRedisWorkers:
    TIME_QUANTAM = 5
    MOMENTUM_THRESHOLD = 3
    VELOCITY_THRESHOLD = 5
    MAX_DYNAMIC_WORKERS = 10
    PENDING_JOBS_TRIGGER = 20

    def __init__(self):
        self.low_q = redis_q.get_queue(name="low")
        # perodically update these values.
        self.pending_jobs = len(self.low_q)
        self.last_velocity = self.velocity
        self.dynamic_workers = []

    @property
    def momentum(self):
        diff = self.velocity - self.last_velocity
        return diff / DynamicRedisWorkers.TIME_QUANTAM

    @property
    def velocity(self):
        curr_pending_jobs = len(self.low_q)
        diff = curr_pending_jobs - self.pending_jobs
        return diff / DynamicRedisWorkers.TIME_QUANTAM

    def need_burst_worker(self):
        app.logger.debug(f"------------ q len {len(self.low_q)}, vel {len(self.velocity)}, mom {len(self.momentum)}")

        return (
            (len(self.low_q) >= DynamicRedisWorkers.PENDING_JOBS_TRIGGER)
            or self.velocity >= self.VELOCITY_THRESHOLD
            or self.momentum >= self.MOMENTUM_THRESHOLD
        )

    def num_burst_worker_needed(self):
        return max(DynamicRedisWorkers.MAX_DYNAMIC_WORKERS, len(self.low_q))

    def spawn_new_workers(self, count, queue_=None):
        if queue_ is None:
            queue_ = self.low_q
        with Connection(connection=redis_q.connection):
            for i in range(count):
                worker_process = multiprocessing.Process(
                    target=Worker(queue_).work,
                    kwargs={"burst": True}
                )
                self.dynamic_workers.append(worker_process)
                worker_process.start()

    def _active_workers(self):
        active_workers = []
        for worker in self.dynamic_workers:
            if worker.is_alive():
                active_workers.append(worker)
        self.dynamic_workers = active_workers
        return len(self.dynamic_workers)

    def perodic_timer(self):
        while True:
            if self.need_burst_worker():
                free_slots = self.MAX_DYNAMIC_WORKERS - self._active_workers()
                if free_slots >= 0:
                    worker_count = free_slots
                else:
                    worker_count = min(free_slots, self.num_burst_worker_needed())
                self.spawn_new_workers(count=worker_count)

                #update peroidic values.
                self.pending_jobs = len(self.low_q)
                self.last_velocity = self.velocity
                time.sleep(DynamicRedisWorkers.TIME_QUANTAM)

if "__main__" == __name__:
    dynamic_workers = DynamicRedisWorkers()
    dynamic_workers.perodic_timer()
