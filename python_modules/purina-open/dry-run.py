import pathspec
import os

with open('.openignore', 'r') as f:
    spec = pathspec.PathSpec.from_lines('gitwildmatch', f)


matches = spec.match_tree('.')

for match in matches:
    print(match)
    os.remove(match)