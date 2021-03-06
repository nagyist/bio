from ..manhatten import (
    manhatten_tourist, parse_tourist_input, output_lcs, lcs_backtrack,
    lcs_path, longest_dag_path, parse_graph, global_alignment_problem, blosum62,
    pam250, local_alignment_problem, levenshtein_distance,
    fitting_alignment_problem, overlap_alignment_problem
)
from ._lib import find_datasets

def test_manhatten_tourist():
    dataset = [(
        """
        4 4
        1 0 2 4 3
        4 6 5 2 1
        4 4 5 2 1
        5 6 8 5 3
        -
        3 2 4 0
        3 2 4 2
        0 7 3 3
        3 3 0 2
        1 3 2 2
        """
    , 34)] + find_datasets("manhatten_tourist")

    for input_sample, output_sample in dataset:
        n, m, down, right = parse_tourist_input(input_sample)
        assert manhatten_tourist(n, m, down, right) == int(output_sample)


def test_output_lcs():
    dataset = [("AACCTTGG ACACTGTGA", "AACTTG")] + find_datasets("output_lcs")

    for input_sample, output_sample in dataset:
        v, w = input_sample.strip().split()
        backtrack = lcs_backtrack(lcs_path(v, w))
        output = output_lcs(backtrack, v, w)
        assert output == output_sample, "{0} != {1}".format(output, output_sample)


def test_longest_dag_path():
    def parse_input(text: str) -> (int, int, str):
        lines = text.splitlines()
        return int(lines[0]), int(lines[1]), "\n".join(lines[2:])

    def parse_output(text: str) -> (int, list):
        lines = text.splitlines()
        return int(lines[0]), [int(x) for x in lines[1].split("->")]

    dataset = [((
        0, 4,
        """
        0->1:7
        0->2:4
        2->3:2
        1->4:1
        3->4:3
        """
    ), (9, [0, 2, 3, 4]))] + find_datasets(
        "longest_dag_path", parse_input, parse_output
    )

    for input_sample, output_sample in dataset:
        source, sink, graph = input_sample
        graph = parse_graph(graph, weighted=True)
        output = longest_dag_path(graph, source, sink)
        assert output == output_sample, "{0} != {1}".format(output, output_sample)


def test_global_alignment_problem():
    dataset = [(
        "PLEASANTLY MEANLY", "8 PLEASANTLY -MEA--N-LY"
    )] + find_datasets("global_alignment_problem")

    for input_sample, output_sample in dataset:
        v, w = input_sample.split()
        score, v_aligned, w_aligned = output_sample.split()
        score = int(score)
        expected_output = (score, v_aligned, w_aligned)
        output = global_alignment_problem(blosum62(), v, w, u=0, o=5)
        assert output == expected_output, "{0} != {1}".format(output, expected_output)


def test_local_alignment_problem():
    dataset = [(
        "MEANLY PENALTY", "15 EANL-Y ENALTY"
    )] + find_datasets("local_alignment_problem")

    for input_sample, output_sample in dataset:
        v, w = input_sample.strip().split()
        score, v_aligned, w_aligned = output_sample.split()
        score = int(score)
        expected_output = (score, v_aligned, w_aligned)
        output = local_alignment_problem(pam250(), v, w, u=0, o=5)
        assert output == expected_output, "{0} != {1}".format(output, expected_output)


def test_fitting_alignment_problem():
    dataset = [(
        "GTAGGCTTAAGGTTA TAGATA", "2 TAGGCTTA TAGA-T-A"
    )] + find_datasets("fitting_alignment_problem")

    for input_sample, output_sample in dataset:
        v, w = input_sample.strip().split()
        score, v_aligned, w_aligned = output_sample.split()
        score = int(score)
        expected_output = (score, v_aligned, w_aligned)
        output = fitting_alignment_problem(v, w, u=0, o=1)
        assert output == expected_output, "{0} != {1}".format(output, expected_output)


def test_overlap_alignment_problem():
    dataset = [(
        "PAWHEAE HEAGAWGHEE", "1 HEAE HEA-"
    )] + find_datasets("overlap_alignment_problem")

    for input_sample, output_sample in dataset:
        v, w = input_sample.strip().split()
        score, v_aligned, w_aligned = output_sample.split()
        score = int(score)
        expected_output = (score, v_aligned, w_aligned)
        output = overlap_alignment_problem(v, w, u=0, o=2)
        assert output == expected_output, "{0} != {1}".format(output, expected_output)


def test_levenshtein_distance():
    dataset = [(
        "PLEASANTLY MEANLY", 5
    )] + find_datasets("levenshtein_distance")

    for input_sample, output_sample in dataset:
        v, w = input_sample.strip().split()
        distance = levenshtein_distance(v, w)
        assert distance == int(output_sample), "{0} != {1}".format(distance, output_sample)


def main():
    #test_manhatten_tourist()
    #test_output_lcs()
    #test_longest_dag_path()
    test_global_alignment_problem()
    test_local_alignment_problem()
    test_levenshtein_distance()
    test_fitting_alignment_problem()
    test_overlap_alignment_problem()
    print("Success!")


if __name__ == '__main__':
    main()
