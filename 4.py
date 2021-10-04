def foo(d):
    match d:
        case None:
            print("Got: None")
        case [3 | 4, *rest]:  # first element 3 or 4 (not 7)
            print(f'{rest=}')
        case {'key': value}:
            print(f"{value=}")
        case ['rm', '--force' | '-f', *files]:
            print("Force removal:: %r" % files)
        case other:
            print("Other: %r" % other)

foo(None)
foo([3, 4, 5, 6, 7])
foo({'key': 12345})
foo(['rm', '-f', 'file1', 'file2'])
foo(['cd', '.'])
