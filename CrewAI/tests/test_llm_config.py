import unittest
from config.llm_config import get_llm
from config.topics import get_topic, get_all_topics
from main import create_content_crew

class TestLLMConfiguration(unittest.TestCase):
    def test_topic_retrieval(self):
        """Test if topics can be retrieved correctly"""
        tech_topic = get_topic("technology")
        self.assertIsNotNone(tech_topic)
        
        all_topics = get_all_topics()
        self.assertTrue(len(all_topics) > 0)
    
    def test_openai_llm(self):
        """Test OpenAI LLM configuration"""
        try:
            result = create_content_crew(
                topic="Artificial Intelligence",
                llm_provider="openai"
            )
            self.assertIsNotNone(result)
        except Exception as e:
            self.fail(f"OpenAI test failed with error: {str(e)}")
    
    def test_huggingface_llm(self):
        """Test HuggingFace LLM configuration"""
        try:
            llm = get_llm("huggingface")
            self.assertIsNotNone(llm)
        except Exception as e:
            self.fail(f"HuggingFace test failed with error: {str(e)}")
    
    def test_mistral_llm(self):
        """Test Mistral LLM configuration"""
        try:
            config = get_llm("mistral")
            self.assertIsNotNone(config)
            self.assertIn("api_key", config)
            self.assertIn("api_base", config)
            self.assertIn("model_name", config)
        except Exception as e:
            self.fail(f"Mistral test failed with error: {str(e)}")
    
    def test_cohere_llm(self):
        """Test Cohere LLM configuration"""
        try:
            llm = get_llm("cohere")
            self.assertIsNotNone(llm)
        except Exception as e:
            self.fail(f"Cohere test failed with error: {str(e)}")

if __name__ == '__main__':
    unittest.main() 