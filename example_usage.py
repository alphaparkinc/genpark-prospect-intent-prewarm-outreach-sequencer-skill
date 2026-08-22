from client import ProspectIntentPrewarmOutreachSequencerClient

def main():
    client = ProspectIntentPrewarmOutreachSequencerClient()
    res = client.score_and_sequence_prospect('globextech.com')
    print('Prospect: ' + res['prospect_domain'] + ' | Intent Tier: ' + res['intent_tier'] + ' (' + str(res['intent_score']) + '/100)')
    print('Predicted Reply Rate: ' + str(res['predicted_reply_rate_pct']) + '%')
    print('Outreach Sequence:')
    for s in res['outreach_sequence']:
        print('  Day ' + str(s['day']) + ' [' + s['channel'] + ']: ' + s['action'])

if __name__ == '__main__':
    main()
