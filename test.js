const fetch = require("node-fetch");
const getResponse = async (message) => {
    try {
      const URL = `https://stormhacks-chatbot.herokuapp.com/get?msg=${message}`;
      const response = await fetch(URL);
      const JSONData = await response.json();
      console.log(JSONData.response);
      return JSONData;
    } catch (err) {
      console.error(err.message);
    }
};

getResponse("ten times 4")


