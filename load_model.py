from happytransformer import HappyGeneration
import psutil

happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-125M")

happy_gen.save("125M")