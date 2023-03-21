{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2bd82ca9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import csv\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c332752c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add a variable to load a file from a path.\n",
    "file_to_load = os.path.join(\"election_results.csv\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d492b61f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add a variable to save the file to a path.\n",
    "file_to_save = os.path.join(\"election_analysis.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7fb36d5c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Initialize a total vote counter.\n",
    "total_votes = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "68b9cc10",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Candidate Options and candidate votes.\n",
    "candidate_options = []\n",
    "candidate_votes = {}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7f59f23b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1: Create a county list and county votes dictionary.\n",
    "county_options = []\n",
    "county_votes = {}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "08b9a84a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Track the winning candidate, vote count and percentage\n",
    "winning_candidate = \"\"\n",
    "winning_count = 0\n",
    "winning_county = 0\n",
    "winning_percentage = 0\n",
    "winning_percentage = 0\n",
    "winning_c_percentage = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4892c573",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2: Track the largest county and county voter turnout.\n",
    "largest_turnout_county = \"\"\n",
    "largest_turn_count = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "caf16aa9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Read the csv and convert it into a list of dictionaries\n",
    "with open(file_to_load) as election_data:\n",
    "    reader = csv.reader(election_data)\n",
    "    header = next(reader)\n",
    "    for row in reader:\n",
    "        total_votes = total_votes + 1\n",
    "        candidate_name = row[2]\n",
    "        county_name = row[1]\n",
    "        if candidate_name not in candidate_options:\n",
    "            candidate_options.append(candidate_name)\n",
    "            candidate_votes[candidate_name] = 0\n",
    "        candidate_votes[candidate_name] += 1 \n",
    "        if county_name not in county_options:\n",
    "            county_options.append(county_name)  \n",
    "            county_votes[county_name] = 0\n",
    "        county_votes[county_name] += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "88f84796",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Election Results\n",
      "-------------------------\n",
      "Total Votes: 369,711\n",
      "-------------------------\n",
      "\n",
      "County Votes:\n",
      "Jefferson: 10.5% (38,855)\n",
      "Denver: 82.8% (306,055)\n",
      "Arapahoe: 6.7% (24,801)\n",
      "\n",
      "-------------------------\n",
      "Largest County Turnout: Denver\n",
      "Winning County Vote: 306,055\n",
      "Winning County Percentage: 82.8%\n",
      "-------------------------\n",
      "\n",
      "Candidate Percentage of Votes:\n",
      "-------------------------\n",
      "\n",
      "Charles Casper Stockham: 23.0% (85,213)\n",
      "\n",
      "Diana DeGette: 73.8% (272,892)\n",
      "\n",
      "Raymon Anthony Doane: 3.1% (11,606)\n",
      "\n",
      "-------------------------\n",
      "Winner: Diana DeGette\n",
      "Winning Vote Count: 272,892\n",
      "Winning Percentage: 73.8%\n",
      "-------------------------\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Save the results to our text file.\n",
    "with open(file_to_save, \"w\") as txt_file:\n",
    "\n",
    "    # Print the final vote count (to terminal)\n",
    "    election_results = (\n",
    "        f\"\\nElection Results\\n\"\n",
    "        f\"-------------------------\\n\"\n",
    "        f\"Total Votes: {total_votes:,}\\n\"\n",
    "        f\"-------------------------\\n\\n\"\n",
    "        f\"County Votes:\\n\")\n",
    "    print(election_results, end=\"\")\n",
    "\n",
    "    txt_file.write(election_results)\n",
    "\n",
    "    # 6a: Write a for loop to get the county from the county dictionary.\n",
    "    for county_name in county_votes:\n",
    "        # 6b: Retrieve the county vote count.\n",
    "        county = county_votes.get(county_name)\n",
    "        # 6c: Calculate the percentage of votes for the county.\n",
    "        county_percentage = float(county) / float(total_votes) * 100\n",
    "        county_results = (\n",
    "            f\"{county_name}: {county_percentage:.1f}% ({county:,})\\n\")\n",
    "\n",
    "         # 6d: Print the county results to the terminal.\n",
    "        print(county_results, end=\"\")\n",
    "         # 6e: Save the county votes to a text file.\n",
    "        txt_file.write(county_results)\n",
    "         # 6f: Write an if statement to determine the winning county and get its vote count.\n",
    "        if (county > winning_county) and (county_percentage > winning_c_percentage):\n",
    "            winning_county = county\n",
    "            winning_c_candidate = county_name\n",
    "            winning_c_percentage = county_percentage\n",
    "                # 7: Print the county with the largest turnout to the terminal.\n",
    "    winning_county_summary = (\n",
    "        f\"\\n-------------------------\\n\"\n",
    "        f\"Largest County Turnout: {winning_c_candidate}\\n\"\n",
    "        f\"Winning County Vote: {winning_county:,}\\n\"\n",
    "        f\"Winning County Percentage: {winning_c_percentage:.1f}%\\n\"\n",
    "        f\"-------------------------\\n\\n\"\n",
    "        f\"Candidate Percentage of Votes:\\n\"\n",
    "        f\"-------------------------\\n\")\n",
    "    print(winning_county_summary)\n",
    "        # 8: Save the county with the largest turnout to a text file.\n",
    "    txt_file.write(winning_county_summary)\n",
    "     # Save the final candidate vote count to the text file.\n",
    "    for candidate_name in candidate_votes:\n",
    "\n",
    "        # Retrieve vote count and percentage\n",
    "        votes = candidate_votes.get(candidate_name)\n",
    "        vote_percentage = float(votes) / float(total_votes) * 100\n",
    "        candidate_results = (\n",
    "            f\"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\\n\")\n",
    "\n",
    "        # Print each candidate's voter count and percentage to the\n",
    "        # terminal.\n",
    "        print(candidate_results)\n",
    "        #  Save the candidate results to our text file.\n",
    "        txt_file.write(candidate_results)\n",
    "\n",
    "        # Determine winning vote count, winning percentage, and candidate.\n",
    "        if (votes > winning_count) and (vote_percentage > winning_percentage):\n",
    "            winning_count = votes\n",
    "            winning_candidate = candidate_name\n",
    "            winning_percentage = vote_percentage\n",
    "\n",
    "    # Print the winning candidate (to terminal)\n",
    "    winning_candidate_summary = (\n",
    "        f\"-------------------------\\n\"\n",
    "        f\"Winner: {winning_candidate}\\n\"\n",
    "        f\"Winning Vote Count: {winning_count:,}\\n\"\n",
    "        f\"Winning Percentage: {winning_percentage:.1f}%\\n\"\n",
    "        f\"-------------------------\\n\")\n",
    "    print(winning_candidate_summary)\n",
    "\n",
    "    # Save the winning candidate's name to the text file\n",
    "    txt_file.write(winning_candidate_summary)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cfd44a89",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
