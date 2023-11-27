from src.insights.jobs import ProcessJobs


def read_pt_file(path):
    process = ProcessJobs()
    process.read(path)
    result = process.jobs_list

    return result
