#!/usr/bin/env python
import os
from flask import Flask, request, make_response, render_template, session, redirect, url_for, json
from events import Event
from api import get_events

#-----------------------------------------------------------------------

app = Flask(__name__) # set up Flask server
app.secret_key = "a secret key for testing" # need to set a secret key in order to use session cookies

#-----------------------------------------------------------------------

# Home
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    events = []

    # Get all data for this date
    date = '02/28' # change this date to get a different date's events
    data = get_events(date)
    
    events_data = data["selected"] # get the list of events
    events_data.sort(key=lambda x: x["year"]) # sort the events by the year
    num_events = len(events_data) # get the total number of events

    birthdate_index = -1 # have not added birthdate into array yet
    
    # Add each event to the events array
    for (index, event) in enumerate(events_data):
        image_link = None # default no link
        event_year = event["year"] # get the year of the event
        if (event_year >= 1999 and birthdate_index < 0):
            # Add birth event in the right position
            birth_event = Event(1999, "Lan's Birthday", "You were born on this day :)", None, None)
            events.append(birth_event)
            birthdate_index = index # remember that birth date has already been added
        event_title = event["pages"][0]["titles"]["normalized"] # get the title of the event
        event_description = event["text"] # get the description of the event
        article_link = event["pages"][0]["content_urls"]["desktop"]["page"] # get the article link of the event
        print(event_title)
        if "originalimage" in event["pages"][0]:
            image_link = event["pages"][0]["originalimage"]["source"] # get the image link of the event, if it exists
        new_event = Event(event_year, event_title, event_description, article_link, image_link) # create a new event with this event info
        print(new_event)
        events.append(new_event) # add this event to the events array
    print(events)
    print(birthdate_index)
    return render_template('index.html', events=events, starting_slide=birthdate_index)