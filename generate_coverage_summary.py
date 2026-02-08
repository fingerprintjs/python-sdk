import json

with open('coverage.json') as f:
    json_report = json.load(f)

json_summary = {
    'total': {'statements': {'pct': round(json_report['totals']['percent_covered'], 2)}}
}

with open('coverage-summary.json', 'w') as json_file:
    json.dump(json_summary, json_file)
