import openai
import g4f

# Set your OpenAI API key
# openai.api_key = "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"

# def generate_reviewer(topic):
#     prompt = f"Generate a reviewer for the topic: {topic}. The reviewer should include an introduction, detailed content for each lesson and chapters with brief discussion, key concepts, definitions and examples, and a summary of the topic."

#     response = openai.Completion.create(
#         engine="text-davinci-003",  # You can experiment with different engines
#         prompt=prompt,
#         temperature=0.9,
#         max_tokens=4000,
#         top_p=0.8
#     )

#     return response.choices[0].text

# # Specify the topic for the reviewer
# topic = "Fundamentals on java programming"

# # Generate the reviewer material
# reviewer_material = generate_reviewer(topic)

# # Print the generated reviewer material
# print(reviewer_material)


def gpt4(topic):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        provider=g4f.Provider.Vercel,
        messages=[
            {
                "role": "user",
                "content": f"Generate a reviewer material and cheat sheet and key concepts and definition of terms and summary for the topic: {topic}",
            }
        ],
    )
    return response

topic = input("Input topic: ")
print(gpt4(topic))

# Generate a reviewer for the topic: fundamentals of java programming. The reviewer should include an introduction, detailed content for each lesson and chapters, key concepts, definitions and examples, and a summary of the topic.
