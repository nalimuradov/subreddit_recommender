import data.final_dict
from flask import Flask, request, render_template

app = Flask(__name__)


# final step: return most similar subs given the subname as input
def get_most_similar_subs(subname):
    relevant = {}
    x = data.final_dict.pairs
    for i in x:
        if subname in i:
            relevant[i] = x[i]

    ordered = sorted(relevant.items(), key=lambda y: y[1])

    most_similar = []
    if len(ordered) > 10:
        for i in range(1, 12):
            most_similar.append(ordered[-i])

    final_values = _parse_names(most_similar, subname)
    return final_values


# helper function
def _parse_names(similar, subname):
    names = []
    counts = []
    for i in similar:
        tmp = list(i[0])
        if tmp[0] == subname:
            names.append(tmp[1])
        else:
            names.append(tmp[0])
        counts.append(i[1])
    return names, counts


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/home', methods=['POST'])
def display():
    subname = request.form.get("similar")
    most_similar = get_most_similar_subs(subname)

    names = most_similar[0]
    counts = most_similar[1]
    pairs = zip(names, counts)

    return render_template('index.html', names=names, counts=counts, subname="/r/" + str(subname), pairs=pairs)


if __name__ == "__main__":
    app.run(debug=True)