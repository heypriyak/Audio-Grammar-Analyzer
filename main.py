import asyncio
from datetime import datetime
from models.voice_sample import VoiceSample
from services.grammar_scoring_engine import GrammarScoringEngine

async def main():
    # Create a test voice sample
    sample = VoiceSample(
        id="test_sample_1",
        audio_data=b"dummy_audio_data",
        transcript="Yesterday I am going to the store and she were happy.",
        duration=5.5,
        sample_rate=44100,
        metadata={
            "speaker_id": "user123",
            "timestamp": datetime.now(),
            "language": "en-US"
        }
    )

    # Initialize the scoring engine
    engine = GrammarScoringEngine()

    # Score the sample
    result = await engine.score_voice_sample(sample)

    # Print results
    print(f"Sample ID: {result.sample_id}")
    print(f"Score: {result.score}")
    print("Errors:")
    for error in result.errors:
        print(f"- Rule: {error.rule}, Text: '{error.text}', Position: {error.position}")

if __name__ == "__main__":
    asyncio.run(main())
