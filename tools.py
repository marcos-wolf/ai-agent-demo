def get_system_status():
    return {
        "status": "operational",
        "cpu_usage": "32%",
        "memory_usage": "58%",
        "message": "All systems are operating normally."
    }


def calculate_sum(a, b):
    return {
        "result": a + b
    }


def execute_tool(name, arguments):
    if name == "get_system_status":
        return get_system_status()

    if name == "calculate_sum":
        return calculate_sum(
            arguments["a"],
            arguments["b"]
        )

    return {
        "error": f"Unknown tool: {name}"
    }
