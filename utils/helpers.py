def format_response_success(data,status="success"):
    return {
        "status": status,
        "data": data
    }
def format_response_fail(code, status="fail"):
    return {
        "status": status,
        "error": code  # 'code' can be an error message, not just the status code
    }

