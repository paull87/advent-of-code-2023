
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
            seeds = [tuple(seeds[:x+1][-2:]) for x in range(1, len(seeds), 2)]
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


def convert_mapping(refs, mappings):
    conversions = []
    ref_copy = refs.copy()
    while ref_copy:
        print(ref_copy)
        print(conversions)
        ref = ref_copy.pop()
        ref_start = ref[0]
        ref_end = ref[1]
        for mapping in mappings:
            source_end = mapping['source_start'] + mapping['range'] - 1
            if (
                mapping['source_start'] <= ref_start <= source_end
                or mapping['source_start'] <= ref_end <= source_end
            ):
                overlap_start = max(mapping['source_start'], ref_start)
                overlap_end = min(source_end, ref_end)
                dest_diff = mapping['destination_start'] - mapping['source_start']
                conversions.append([overlap_start + dest_diff, overlap_end + dest_diff])
                # trim the ref range to reflect the already converted section
                if ref_start == overlap_start and ref_end == overlap_end:
                    ref_start = ref_end
                if ref_end > overlap_end:
                    ref_copy.append([overlap_end + 1, ref_end])
                    ref_end = overlap_end - 1
                if overlap_start >= ref_start:
                    ref_end = overlap_start - 1
            if ref_start >= ref_end:
                break
        if ref_start < ref_end:
            conversions.append([ref_start, ref_end])
    return conversions


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
        seed_start = seed[0]
        seed_range = seed[1]
        seed_end = seed_start + seed_range - 1
        seed_mappings[seed] = {}
        for step in mapping_steps:
            source_ref = seed_mappings[seed].get(previous_step) or [[seed_start, seed_end]]
            seed_mappings[seed][step] = convert_mapping(source_ref, maps[step])
            if seed_range != sum(x[1] - x[0] + 1 for x in seed_mappings[seed][step]):
                import pdb; pdb.set_trace()
            previous_step = step
    return seed_mappings


if __name__ == '__main__':
    from pprint import pprint
    result = main()
    pprint(result)
    # import pdb;pdb.set_trace()
    print(sorted([y[0] for x in result.values() for y in x['humidity-to-location']]))
    print('Min Location:', min([y[0] for x in result.values() for y in x['humidity-to-location']]))