from bitarray import bitarray, util
import math


def read_lines(path):
    with open(path) as f:
        lines = f.read()
    return lines.strip()


def parse_input(input: str) -> bitarray:
    bits = util.hex2ba(input)
    return bits


class PACKET:
    def __init__(self, bits: bitarray) -> None:
        self.origin = bits
        self.version = util.ba2int(bits[:3])
        self.type_id = util.ba2int(bits[3:6])
        self.literal_value = None
        self.operator_type = None
        self.extra_bits = bitarray()
        self.child_packets = []
        self._parse_packets(bits[6:])

    def __repr__(self) -> str:
        if self.type_id == 4:
            return f"Packet {self.version}, Literal_value: {self.literal_value}"
        else:
            return f"Packet v:{self.version}, operator type: {self.operator_type} Children num: {len(self.child_packets)}"

    def _parse_packets(self, bits: bitarray) -> None:
        if self.type_id == 4:
            self._parse_literals(bits)
        else:
            self.operator_type = bits[0]
            if self.operator_type == 0:
                self._parse_operator_type0(bits[1:])
            elif self.operator_type == 1:
                self._parse_operator_type1(bits[1:])

    def _parse_literals(self, bits: bitarray) -> None:
        literal = bitarray()
        stop_bit = 1
        idx = 0
        while stop_bit == 1:
            stop_bit = bits[idx]
            literal += bits[idx + 1 : idx + 5]
            idx += 5
        self.literal_value = util.ba2int(literal)
        self.extra_bits = bits[idx:]

    def _parse_operator_type0(self, bits: bitarray) -> None:
        sub_packets_length = util.ba2int(bits[:15])
        sub_packet = bits[15 : 15 + sub_packets_length]
        while any(sub_packet):
            new_packet = PACKET(sub_packet)
            self.child_packets.append(new_packet)
            sub_packet = new_packet.extra_bits
        self.extra_bits = bits[15 + sub_packets_length :]

    def _parse_operator_type1(self, bits: bitarray) -> None:
        num_sub_packets = util.ba2int(bits[:11])
        sub_packet = bits[11:]
        for x in range(num_sub_packets):
            new_packet = PACKET(sub_packet)
            self.child_packets.append(new_packet)
            sub_packet = new_packet.extra_bits
        self.extra_bits = sub_packet

    def _total_version(self) -> int:
        version = self.version
        version += sum([c._total_version() for c in self.child_packets])
        return version

    def _value(self) -> int:
        # if the packet is a literal packet then i return the literal value
        if self.type_id == 4:
            return self.literal_value

        # get all the values of all the children of this packet
        child_sub_packets = [c._value() for c in self.child_packets]

        if self.type_id == 0:
            return sum(child_sub_packets)
        elif self.type_id == 1:
            return math.prod(child_sub_packets)
        elif self.type_id == 2:
            return min(child_sub_packets)
        elif self.type_id == 3:
            return max(child_sub_packets)
        elif self.type_id == 5:
            return child_sub_packets[0] > child_sub_packets[1]
        elif self.type_id == 6:
            return child_sub_packets[0] < child_sub_packets[1]
        elif self.type_id == 7:
            return child_sub_packets[0] == child_sub_packets[1]


def part1(bits: bitarray) -> int:
    p = PACKET(bits)
    solution1 = p._total_version()
    return solution1


def part2(bits: bitarray) -> int:
    p = PACKET(bits)
    solution2 = p._value()
    return solution2


test_inputs_1 = [
    "8A004A801A8002F478",
    "620080001611562C8802118E34",
    "C0015000016115A2E0802F182340",
    "A0016C880162017C3686B18A3D4780",
]

expec_results_1 = [16, 12, 23, 31]

# test for part 1
for idx, (t, e) in enumerate(zip(test_inputs_1, expec_results_1)):
    solution = part1(parse_input(t))
    assert solution == e, f"test {idx} failed,\n expected: {e}\n actual: {solution}"


test_inputs_2 = [
    "C200B40A82",
    "04005AC33890",
    "880086C3E88112",
    "CE00C43D881120",
    "D8005AC2A8F0",
    "F600BC2D8F",
    "9C005AC2F8F0",
    "9C0141080250320F1802104A08",
]

expec_results_2 = [3, 54, 7, 9, 1, 0, 0, 1]

for idx, (t, e) in enumerate(zip(test_inputs_2, expec_results_2)):
    solution = part2(parse_input(t))
    assert solution == e, f"test {idx} failed,\n expected: {e}\n actual: {solution}"

print("ALL TEST PASSED")

input_path = "day_16/input.txt"
input = parse_input(read_lines(input_path))
print(f"solution1: {part1(input)}")
print(f"solution2: {part2(input)}")
