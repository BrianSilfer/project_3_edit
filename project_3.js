//import bb from 'billboard.js';


const stocksData = "http://127.0.0.1:5000/stocks";
const movieData = "http://127.0.0.1:5000/movies";
// 2015
const stocksData15 = "http://127.0.0.1:5000/stocks/date/start=2014/stop=2015";
const movieData15 = "http://127.0.0.1:5000/movies/added/start=2014/stop=2015";
// 2016
const stocksData16 = "http://127.0.0.1:5000/stocks/date/start=2015/stop=2016";
const movieData16 = "http://127.0.0.1:5000/movies/added/start=2015/stop=2016";
// 2017
const stocksData17 = "http://127.0.0.1:5000/stocks/date/start=2016/stop=2017";
const movieData17 = "http://127.0.0.1:5000/movies/added/start=2016/stop=2017";
// 2018
const stocksData18 = "http://127.0.0.1:5000/stocks/date/start=2017/stop=2018";
const movieData18 = "http://127.0.0.1:5000/movies/added/start=2017/stop=2018";
// 2019
const stocksData19 = "http://127.0.0.1:5000/stocks/date/start=2018/stop=2019";
const movieData19 = "http://127.0.0.1:5000/movies/added/start=2018/stop=2019";



function pagechart(dataset) {
  let data; 
  let stock_data;
  if (dataset === '2015') {
    data = movieData15
    stock_data = stocksData15
  }
  if (dataset === '2016') {
    data = movieData16
    stock_data = stocksData16
  }
  if (dataset === '2017') {
    data = movieData17
    stock_data = stocksData17
  }
  if (dataset === '2018') {
    data = movieData18
    stock_data = stocksData18
  }
  else if (dataset === '2019') {
    data = movieData19
    stock_data = stocksData19
  }
  d3.json(stock_data).then((stocks) => {
    //check that data loaded
    console.log(stocks);
    
    //create empty list for dates and adjusted close
    let dates = [];
    let adj_close = [];
    stocks.forEach(item => {
      //extract date and adj_close from json
      let date = item.Date;
      let adj_c = item.Adj_close;
      //push date and adj_close to lists for visualizatio n
      dates.push(date);
      adj_close.push(adj_c);
      //to visualize x and y data in billboard.js, a header must be added to the first spot
      //in each array
      
    });
    dates.unshift("date");
    adj_close.unshift("adj_close");
    console.log(dates)
    console.log(adj_close)
    const stock_chart = bb.generate({
      title: {
        text: "Netlfix Stock Chart"
      },
        data: {
            columns: [
                dates,
                adj_close
                
            ],
            type: "line"
        },
        bar: {
            width: {
                ratio: 0.5
            }
        },
        bindto: "#lineChart"
    });
  });
    //pulling movies data from
  d3.json(data).then((titles_data) => {
    //check that data loaded
  console.log(titles_data)
  
  



// Step 1: Create an empty list to store the country counts
  country_count = {};
  rating_list = [];
  const ratingsCount = {};
// Step 2: Loop through the array of objects
  titles_data.forEach(item => {
  // Step 3: Extract the "country" property value
      let country = item.country;
      let rating = item.rating;
        
  // Step 4: Check if the country already exists in the counts object
      if (country !== null && country !== undefined) {
          if (country_count[country]) {
      // Increment the count if the country already exists
            country_count[country]++;
      } else {
      // Add the country as a new key with a count of 1 if it doesn't exist
      country_count[country] = 1;
      rating_list.push(rating);
    
  
  // Count the occurrences of each rating
      rating_list.forEach(rating => {
      if (ratingsCount[rating]) {
        ratingsCount[rating]++;
      } else {
        ratingsCount[rating] = 1;
      }
      
  });  
        
    }
    
  
  };
});
const ratingsArray = Object.entries(ratingsCount);

console.log(ratingsArray);
console.log(ratingsCount);
console.log(country_count);

// converting dictionary to list
const country_array = Object.entries(country_count);
//sort data in descending order
country_array.sort((a, b) => b[1] - a[1]);
    const piechart = bb.generate({
      title: {
        text: "Netflix Show Ratings Distribution"
      },
      data: {
        columns:[
          ratingsArray[0],
          ratingsArray[1],
          ratingsArray[2],
          ratingsArray[3],
          ratingsArray[4],
          ratingsArray[5],
          ratingsArray[6],
          ratingsArray[7],
        ],
        type:"pie"
      },
      bindto: "#pieChart"

      });

console.log(country_array);
    const chart = bb.generate({
      title: {
        text: "Netlfix Production Locations"
      },
        data: {
            columns: [
                country_array[0],
                country_array[1],
                country_array[2],
                country_array[3],
                country_array[4],
                country_array[5],
                country_array[6],
                country_array[7],
                country_array[8],
                country_array[9],
                
            ],
            type: "bar"
        },
        bar: {
            width: {
                ratio: 0.5
            }
        },
        bindto: "#barChart"
});


}); 

}
pagechart('2015');

function OnChange (selected){
  pagechart(selected);

}
