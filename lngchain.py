# Import the necessary libraries
import os
import sys
import json
import requests

# Define the function to create the agent
def create_agent(file_path):
  """Creates an agent that can answer questions based on the content of a file
  """

  # Read the file content
  with open(file_path, "r") as f:
    content = f.read()
    
  agent = {
      "name": "Agent",
      "content": content,
  }

  
  return agent

# Define the function to answer a question
def answer_question(agent, question):
  """Answers a question using the agent.

  Args:
    agent: The agent object.
    question: The question to answer.

  Returns:
    The answer to the question.
  """

  # Find the answer in the agent content
  answer = None
  for sentence in agent["content"].split("."):
    if question in sentence:
      answer = sentence
      break

  # If no answer is found, return a default answer
  if answer is None:
    return "I don't know the answer to that question."

  # Return the answer
  return answer

# Define the main function
def main():
  # Get the file path from the user
  file_path = input("Enter the path to the file: ")

  # Create the agent
  agent = create_agent(file_path)

  # Get the question from the user
  question = input("Enter your question: ")

  # Answer the question
  answer = answer_question(agent, question)

  
  print(answer)


if __name__ == "_main_":
  main()
