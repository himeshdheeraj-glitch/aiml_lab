# Bayesian Network: Burglary, Earthquake, Alarm, David, Sophia

# Prior probabilities
P_burglary = 0.002
P_earthquake = 0.001

# Conditional probabilities of Alarm
P_alarm_B_E = 0.94
P_alarm_B_NE = 0.95
P_alarm_NB_E = 0.31
P_alarm_NB_NE = 0.01

# Conditional probabilities of David calling
P_D_C_alarm = 0.91
P_D_NC_alarm = 0.09
P_D_C_noalarm = 0.01
P_D_NC_noalarm = 0.99

# Conditional probabilities of Sophia calling
P_S_C_alarm = 0.75
P_S_NC_alarm = 0.25
P_S_C_noalarm = 0.02
P_S_NC_noalarm = 0.98


def validate_probability(p):
    if not 0 <= p <= 1:
        raise ValueError(
            "Invalid probability: P must be between 0 and 1"
        )


def joint_probability(alarm, B, E, D, S):
    # Validate prior probabilities
    validate_probability(P_burglary)
    validate_probability(P_earthquake)

    # Probability of burglary
    p_B = P_burglary if B else 1 - P_burglary

    # Probability of earthquake
    p_E = P_earthquake if E else 1 - P_earthquake

    # Probability of alarm given burglary and earthquake
    if B and E:
        p_alarm = P_alarm_B_E
    elif B and not E:
        p_alarm = P_alarm_B_NE
    elif not B and E:
        p_alarm = P_alarm_NB_E
    else:
        p_alarm = P_alarm_NB_NE

    validate_probability(p_alarm)

    # Probability of alarm or no alarm
    p_A = p_alarm if alarm else 1 - p_alarm

    # Probability of David calling
    if alarm:
        p_D = P_D_C_alarm if D else P_D_NC_alarm
    else:
        p_D = P_D_C_noalarm if D else P_D_NC_noalarm

    # Probability of Sophia calling
    if alarm:
        p_S = P_S_C_alarm if S else P_S_NC_alarm
    else:
        p_S = P_S_C_noalarm if S else P_S_NC_noalarm

    validate_probability(p_D)
    validate_probability(p_S)

    # Calculate joint probability
    return p_B * p_E * p_A * p_D * p_S


def run_test(test_name, expected_type, **kwargs):
    try:
        result = joint_probability(**kwargs)

        print(f"{test_name}: {expected_type}")
        print(f"Joint Probability = {result:.10f}\n")

    except Exception as e:
        print(f"{test_name}: Error: {e}\n")


# Test Case 1
run_test(
    "TC1", "Success",
    alarm=True, B=False, E=False, D=True, S=True
)

# Test Case 2
run_test(
    "TC2", "Success",
    alarm=True, B=True, E=False, D=True, S=True
)

# Test Case 3
run_test(
    "TC3", "Success",
    alarm=True, B=False, E=True, D=True, S=False
)

# Test Case 4: Invalid probability
P_alarm_NB_E = 1.5

run_test(
    "TC4", "Failure",
    alarm=True, B=False, E=True, D=True, S=True
)

# Restore valid probability
P_alarm_NB_E = 0.31

# Test Case 5: Valid probability check
run_test(
    "TC5", "Success",
    alarm=False, B=False, E=False, D=False, S=False
)