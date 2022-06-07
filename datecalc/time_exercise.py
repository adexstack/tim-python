from time import get_clock_info

print(get_clock_info('monotonic'))
print(get_clock_info('process_time'))
print(get_clock_info('perf_counter'))
print(get_clock_info('time'))