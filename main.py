"""Local CLI entry point for the Policy Compliance Checker."""

from dotenv import load_dotenv

load_dotenv()

from policy_checker.graph import graph

SAMPLE_TEXT = """\
Dear hiring manager,

My name is John Smith and you can reach me at john.smith@example.com or call \
me at (555) 123-4567. My SSN is 123-45-6789 and my credit card number is \
4111-1111-1111-1111.

I believe those people from the other side are all liars and cheats who \
deserve whatever bad things come to them. They are fundamentally inferior \
and should be excluded from society. Anyone who disagrees is a traitor and \
will face consequences.

Please wire $50,000 to my account immediately or I will expose your company's \
secrets. This is not a threat, it's a promise. You have 24 hours to comply.

Best regards,
John Smith
Server IP: 192.168.1.100\
"""


def main() -> None:
    print("=" * 60)
    print("Policy Compliance Checker")
    print("=" * 60)

    result = graph.invoke({"input_text": SAMPLE_TEXT})

    print("\n--- PII Findings ---")
    for finding in result["pii_findings"]:
        print(f"  [{finding['type']}] \"{finding['match']}\" (pos {finding['start']}-{finding['end']})")

    print("\n--- Redacted Text ---")
    print(result["redacted_text"])

    print("\n--- Rhetoric Analysis ---")
    print(result["rhetoric_findings"])

    print("\n--- Final Review & Suggestions ---")
    print(result["review_summary"])


if __name__ == "__main__":
    main()
