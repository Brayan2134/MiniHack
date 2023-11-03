import os
import openai
openai.api_key = "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"
continueProgram = "y"

def openAIReq(prompt):
    output = openai.Completion.create(
        engine="davinci",  # Choose the model/engine you want to use
        prompt= prompt,
        max_tokens=50  # Set the maximum length of the generated text
    )
    print("\n" + output.choices[0].text + "\n")

while (continueProgram == "y"):

    openAIPrompt = input("What do you want to know: ")
    openAIReq(openAIPrompt)

    continueProgram = input("Do you wish to continue? (y/n): ")