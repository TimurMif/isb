import constants
import func_for_file
import nist_tests


def main():
    try:
        seqc = func_for_file.read_from_file(constants.PATH_TO_READ_SEQC)
        seqj = func_for_file.read_from_file(constants.PATH_TO_READ_SEQJ)

        print("\nResult frequency NIST tests:")
        print("C++ sequence: ", nist_tests.frequency_test(seqc))
        print("Java sequence: ", nist_tests.frequency_test(seqj))
        print("\nResult identical bits NIST tests:")
        print("C++ sequence: ", nist_tests.identical_bits_test(seqc))
        print("Java sequence: ", nist_tests.identical_bits_test(seqj))
        print("\nResult long sequence NIST tests:")
        print("C++ sequence: ", nist_tests.long_sequence_test(seqc))
        print("Java sequence: ", nist_tests.long_sequence_test(seqj))

        func_for_file.write_report_in_file(constants.PATH_TO_WRITE,
                                           "Result frequency NIST tests:",
                                           nist_tests.frequency_test(seqc),
                                           nist_tests.frequency_test(seqj))
        func_for_file.write_report_in_file(constants.PATH_TO_WRITE,
                                           "\n\nResult identical bits NIST tests:",
                                           nist_tests.identical_bits_test(seqc),
                                           nist_tests.identical_bits_test(seqj))
        func_for_file.write_report_in_file(constants.PATH_TO_WRITE,
                                           "\n\nResult long sequence NIST tests:",
                                           nist_tests.long_sequence_test(seqc),
                                           nist_tests.long_sequence_test(seqj))
    except ValueError as error:
        print(f"{error}")

if __name__ == "__main__":
    main()