import openai
import os

# Shared Memory (akin to long-term memory)
shared_memory = []

# Dynamic Weights (akin to synaptic weights)
dynamic_weights = {}

# Uncomment to Initialize OpenAI API
# openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to generate data using OpenAI API
def generate_data_from_openai(prompt):
    try:
        generated_data = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50,
            temperature=0.7
        )
        return generated_data.choices[0].text.strip()
    except Exception as e:
        print("Error generating data:", e)
        return None

# Learning and Adaptation Function (akin to neural plasticity)
def adapt_and_learn(output, memory, weights):
    if output not in memory:
        memory.append(output)
    else:
        memory.append(output)

    for word in output.split():
        if word in weights:
            weights[word] += 1

# Main Loop for Algorithmic Recurrence (akin to cognitive cycles)
while True:
    try:
        print("Options:")
        print("1. Generate thoughts")
        print("2. Add a thought")
        print("0. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 0:
            break
        elif choice == 1:
            iterations = int(input("Enter the number of loops: "))
            
            previous_output = None

            for i in range(iterations):
                if previous_output:
                    prompt = f"Generate a thought based on previous thoughts: {previous_output}"
                else:
                    prompt = "Generate an initial thought"

                # Introduce dynamic prompts based on shared memory
                dynamic_prompt = '\n'.join(shared_memory[-10:])  # Using the last 10 outputs as dynamic prompts
                prompt += f"\nDynamic Prompt:\n{dynamic_prompt}"

                new_input_data = generate_data_from_openai(prompt)

                transformed_input = []
                for word in new_input_data.split():
                    if word in dynamic_weights:
                        transformed_input.append(word + f"({dynamic_weights[word]})")
                    else:
                        transformed_input.append(word)
                new_output = ' '.join(transformed_input)

                adapt_and_learn(new_output, shared_memory, dynamic_weights)

                shared_memory.append(new_output)
                previous_output = new_output

                print(f"Iteration {i+1} Output:", new_output)
        elif choice == 2:
            new_thought = input("Enter your thought: ")
            shared_memory.append(new_thought)
            print("Thought added to shared memory.")
        else:
            print("Invalid choice. Please enter a valid option.")
            
    except ValueError:
        print("Invalid input. Please enter a valid choice.")
