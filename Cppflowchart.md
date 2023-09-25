```mermaid
graph TD
    Start --> Initialize[Initialize sum and average to 0]
    Initialize --> Display[Display "Please enter 10 numbers:"]
    Display --> SetI[Set i to 0]
    SetI --> CheckI[Is i < 10?]
    CheckI -- Yes --> Read[Read numbers[i]]
    Read --> Add[Add numbers[i] to sum]
    Add --> IncrementI[Increment i]
    IncrementI --> CheckI
    CheckI -- No --> Calculate[Calculate average = sum / 10]
    Calculate --> DisplaySum[Display "The sum is [sum]"]
    DisplaySum --> DisplayAvg[Display "The average is [average]"]
    DisplayAvg --> End[End]
    CheckI -- Yes --> Read
    End --> Stop[Stop]
