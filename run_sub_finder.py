import data.final_dict
import data.subcounts
import numpy
from flask import Flask, request, render_template
import scipy.stats as st
import math

app = Flask(__name__)


# return most similar subs given the subname as input
def get_most_similar_subs(subname):
    relevant = {}
    x = data.final_dict.pairs
    for i in x:
        if subname in i:
            relevant[i] = x[i]

    ordered = sorted(relevant.items(), key=lambda y: y[1])

    most_similar = []
    if len(ordered) > 20:
        for i in range(1, 22):
            most_similar.append(ordered[-i])
    else:
        for i in range(len(ordered)):
            most_similar.append(ordered[-i])

    names = []
    counts = []

    for i in most_similar:
        tmp = list(i[0])
        if tmp[0] == subname:
            names.append(tmp[1])
        else:
            names.append(tmp[0])
        counts.append(i[1])

    subcounts = data.subcounts.subcounts

    for i in range(len(counts)):
        try:
            counts[i] = counts[i] / subcounts[names[i]]
        except:
            counts[i] = counts[i] / 10000

    mean = 0
    if len(counts) > 0:
        mean = numpy.mean(counts)
    stdev = numpy.std(counts)

    new_counts = []
    for i in range(len(counts)):
        if stdev == 0:
            stdev = 1
        z_score = (counts[i] - mean) / stdev
        norm = st.norm.sf(z_score)
        new_counts.append(int(100 * (1 - norm)))

    try:
        new_counts, names = zip(*sorted(zip(new_counts, names)))
    except:
        new_counts, names = [], []

    temp_1 = []
    temp_2 = []

    if len(new_counts) > 9:
        for i in range(1, 11):
            temp_1.append(names[-i])
            temp_2.append(new_counts[-i])
    else:
        for i in range(1, len(new_counts) + 1):
            temp_1.append(names[-i])
            temp_2.append(new_counts[-i])

    names = temp_1
    counts = temp_2

    return names, counts


# default route
@app.route('/')
def home():
    return render_template('base.html')


# route on submit
@app.route('/home', methods=['POST'])
def display():
    subname = request.form.get("similar")
    most_similar = get_most_similar_subs(subname)

    list_string = ""

    names = most_similar[0]
    counts = most_similar[1]
    pairs = zip(names, counts)

    if len(names) == 0:
        list_string = "There was either a misspelling in the subreddit (case-sensitive!), or there is not enough data in /r/" + str(subname) + " to draw a conclusion."
    else:
        list_string = "If you like /r/" + str(subname) + ", you may also enjoy..."

    return render_template('index.html', names=names, counts=counts, subname=list_string, pairs=pairs)


if __name__ == "__main__":
    app.run(debug=True)
