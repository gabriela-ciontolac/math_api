from prometheus_client import Counter, Histogram

# Counter: How many times each operation is called
operation_counter = Counter(
    "math_operation_total",
    "Total number of times each math operation was called",
    ["operation"]
)

# Histogram: Track duration for each operation type
operation_duration = Histogram(
    "math_operation_duration_seconds",
    "Time spent processing each math operation",
    ["operation"]
)