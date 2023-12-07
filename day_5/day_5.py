
input_file = 'input.txt'

with open(input_file) as file:
    input_data = file.readlines()


def parse_data(text):
    mappings = {}
    mapping_name = None
    for line in text:
        line = line.strip()
        if not line:
            continue
        # parse seeds
        if line.startswith('seeds:'):
            seeds = [int(x) for x in line.split()[1:]]
            continue
        if 'map' in line:
            mapping_name = line.split('map')[0].strip()
            mappings[mapping_name] = []
        else:
            dest_start, source_start, map_range = line.split()
            mappings[mapping_name].append(
                {
                    "source_start": int(source_start),
                    "destination_start": int(dest_start),
                    "range": int(map_range),
                }
            )
    return seeds, mappings


def convert_mapping(ref, mappings):
    for mapping in mappings:
        source_end = mapping['source_start'] + mapping['range']
        if mapping['source_start'] <= ref <= source_end:
            dest_diff = mapping['destination_start'] - mapping['source_start']
            return ref + dest_diff
    return ref


def main():
    seeds, maps = parse_data(input_data)
    pprint(maps)
    mapping_steps = [
        'seed-to-soil',
        'soil-to-fertilizer',
        'fertilizer-to-water',
        'water-to-light',
        'light-to-temperature',
        'temperature-to-humidity',
        'humidity-to-location'
    ]
    seed_mappings = {}
    previous_step = ''
    for seed in seeds:
        seed_mappings[seed] = {}
        for step in mapping_steps:
            source_ref = seed_mappings[seed].get(previous_step) or seed
            seed_mappings[seed][step] = convert_mapping(source_ref, maps[step])
            previous_step = step
    return seed_mappings


if __name__ == '__main__':
    from pprint import pprint
    result = main()
    pprint(result)

    print('Min Location:', min([x['humidity-to-location'] for x in result.values()]))