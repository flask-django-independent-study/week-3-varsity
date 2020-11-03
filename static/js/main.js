window.addEventListener('DOMContentLoaded', () => {
  // We are wrapping everything in an event listener 'DOMContentLoaded'
  // This ensures that the window is loaded before we try to connect
  // and set sockets

  // TODO: create a calculatePercentage function that takes in results and sets
  // the width of the progress bar along with the innerHTML

  // TODO: create an updateCandidates function that takes in cadidates and sets
  // the candidates image and name

  // TODO: make an axios get request to '/results' to get the voting results
  //  then pass the data to calculatePercentage to update the results on the page

  // TODO: create a getCandidates function. In the function make an axios get request
  // to '/candidates' and pass the data to updateCandidates

  // TODO: call the getCandidates function

  // TODO: connect to sockets

  // TODO: add an event listener on vote1 that will emit a vote on click

  // TODO: add an event listener on vote2 that will emit a vote on click

  // TODO: create a socket on 'vote_results' function that takes in results and
  // passes the data to calculatePercentage

  // TODO: create an event listener on upload that will getCandidates
})
