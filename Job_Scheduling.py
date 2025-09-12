class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit


def job_scheduling(jobs, n):
    """Solve Job Scheduling Problem using Greedy approach."""

    # Step 1: Sort jobs in descending order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Step 2: Find maximum deadline to create time slots
    max_deadline = max(job.deadline for job in jobs)
    slots = [-1] * (max_deadline + 1)  # -1 means empty slot

    total_profit = 0
    scheduled_jobs = []

    # Step 3: Assign jobs to slots
    for job in jobs:
        # Find a free slot from job.deadline down to 1
        for t in range(job.deadline, 0, -1):
            if slots[t] == -1:
                slots[t] = job.job_id
                total_profit += job.profit
                scheduled_jobs.append(job.job_id)
                break

    return scheduled_jobs, total_profit


# Example usage
if __name__ == "__main__":
    jobs = [
        Job('J1', 2, 100),
        Job('J2', 1, 19),
        Job('J3', 2, 27),
        Job('J4', 1, 25),
        Job('J5', 3, 15)
    ]
    scheduled_jobs, total_profit = job_scheduling(jobs, len(jobs))

    print("Jobs scheduled:", scheduled_jobs)
    print("Total Profit:", total_profit)
