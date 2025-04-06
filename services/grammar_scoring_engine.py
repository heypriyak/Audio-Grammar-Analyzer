import re
from typing import List, Dict
from dataclasses import dataclass
from models.voice_sample import VoiceSample

@dataclass
class GrammarError:
    rule: str
    position: int
    text: str

@dataclass
class ScoringResult:
    sample_id: str
    score: float
    errors: List[GrammarError]

class GrammarScoringEngine:
    def __init__(self):
        self.grammar_rules: Dict[str, re.Pattern] = {}
        self._initialize_grammar_rules()

    def _initialize_grammar_rules(self) -> None:
        self.grammar_rules = {
            'subject_verb_agreement': re.compile(r'\b(he|she|it)\s+(am|are|were)\b', re.IGNORECASE),
            'article_usage': re.compile(r'\b(a\s+[aeiou]|an\s+[^aeiou])\b', re.IGNORECASE),
            'tense_consistency': re.compile(r'\b(yesterday|last week)\s+((am|is|are)\s+\w+ing)\b', re.IGNORECASE)
        }

    async def score_voice_sample(self, sample: VoiceSample) -> ScoringResult:
        errors: List[GrammarError] = []
        transcript = sample.transcript

        for rule_name, pattern in self.grammar_rules.items():
            for match in pattern.finditer(transcript):
                errors.append(GrammarError(
                    rule=rule_name,
                    position=match.start(),
                    text=match.group()
                ))

        return ScoringResult(
            sample_id=sample.id,
            score=self._calculate_score(errors, len(transcript)),
            errors=errors
        )

    def _calculate_score(self, errors: List[GrammarError], text_length: int) -> float:
        base_score = 100
        deduction_per_error = 10
        score = base_score - (len(errors) * deduction_per_error)
        return max(0, score)
