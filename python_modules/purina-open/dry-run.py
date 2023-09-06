# a script to do a dry run to see what files would be deleted when following openignore.txt rules
import pathspec

with open('openignore.txt', 'r') as f:
    spec = pathspec.PathSpec.from_lines('gitwildmatch', f)


matches = spec.match_tree('.')

for match in matches:
    print(match)