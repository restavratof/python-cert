from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple

print('-'*10, 'platform:')
# platform(aliased=False, terse=False)
# aliased→ when set to True (or any non-zero value) it may cause the function to present the alternative underlying layer names instead of the common ones;
# terse→ when set to True (or any non-zero value) it may convince the function to present a briefer form of the result (if possible)
print(platform())
print(platform(1))
print(platform(0,1))
print(platform(1,1))

print('-'*10, 'machine:')
print(machine())

print('-'*10, 'processor:')
print(processor())

print('-'*10, 'system:')
print(system())

print('-'*10, 'OS version:')
print(version())

print('-'*10, 'Python:')
print(python_implementation())
print(python_version_tuple())

