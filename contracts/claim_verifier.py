from genlayer import *


class Contract(gl.Contract):
    verified_claims: dict

    def __init__(self):
        self.verified_claims = {}

    @gl.public.write
    def verify_claim(self, claim: str, source_url: str):
        """
        Verify whether a supplied web page contains evidence supporting
        a factual claim.

        The web request is executed independently by validators.
        Consensus is reached on the final boolean result.
        """

        if not claim.strip():
            raise Exception("Claim cannot be empty")

        if not source_url.startswith(("http://", "https://")):
            raise Exception("A valid HTTP or HTTPS source URL is required")

        def evaluate_source():
            page = gl.nondet.web.render(
                source_url,
                mode="text"
            )

            if not page:
                return False

            normalized_page = page.lower()
            normalized_claim = claim.lower()

            # First check whether the complete claim appears directly.
            if normalized_claim in normalized_page:
                return True

            # For longer claims, require substantial word overlap.
            words = [
                word.strip(".,!?;:\"'()[]{}")
                for word in normalized_claim.split()
            ]

            words = [
                word for word in words
                if len(word) >= 4
            ]

            if not words:
                return False

            matches = sum(
                1 for word in words
                if word in normalized_page
            )

            return matches / len(words) >= 0.60

        verified = gl.eq_principle.strict_eq(evaluate_source)

        self.verified_claims[claim] = {
            "source": source_url,
            "verified": verified,
        }

        return {
            "claim": claim,
            "source": source_url,
            "verified": verified,
        }

    @gl.public.view
    def get_verification(self, claim: str):
        return self.verified_claims.get(
            claim,
            {
                "error": "Claim has not been verified"
            }
        )
