const url_container = $("#url_container");
const value_lower_container = $("#sensor_value_lower");
const value_upper_container = $("#sensor_value_upper");

function updateChart(sensor_id) {
  request = {
    "sensor-id": sensor_id,
    "number-start": document.getElementById("number_start").value,
    "number-end": document.getElementById("number_end").value,
    "date-start": document.getElementById("date_start").value,
    "date-end": document.getElementById("date_end").value,
  };
  $.get(url_container.data("posts-url"), request, function (data) {
    let items = [];
    chartLabels.length = 0;
    dataLabels.length = 0;
    const table = document.getElementById("table_data");
    $.each(data, function (key, val) {
      let arduino_date_value=val.arduino_date.replace("T", " ").split(".")[0].split("+")[0];
      let server_date_value =val.server_date.replace("T", " ").split(".")[0];
      let a = new Date(arduino_date_value);
      let s = new Date(server_date_value);
      let row = table.insertRow();
      let id = row.insertCell(0);
      id.innerHTML = val.id;
    

      
      let value = row.insertCell(1);
      value.innerHTML = val.value;

      let arduino_date = row.insertCell(2);
      arduino_date.innerHTML = arduino_date_value

      let server_date = row.insertCell(3);
      server_date.innerHTML = server_date_value

      let exceed = row.insertCell(4);
      if (value_upper_container.data("value-upper")>val.value && val.value>value_lower_container.data("value-lower")){
        exceed.innerHTML = "False";
      }
      else{
        exceed.innerHTML = "True";
      }
        

      let delta_time = row.insertCell(5);
      delta_time.innerHTML = (s-a)/1000;

      chartLabels.push(arduino_date_value);
      dataLabels.push(val.value);
    });
    chartLabels=chartLabels.reverse()
    dataLabels=dataLabels.reverse()
    chartLabels.length=20;
    dataLabels.length=20;
    chartLabels=chartLabels.reverse()
    dataLabels=dataLabels.reverse()
    myChart.update();
  });
}

function loadTableData(items) {
  items.forEach((item) => {});
}
let chartLabels = [];

let dataLabels = [];

labels = chartLabels;
data = {
  labels: labels,
  datasets: [
    {

      label: "Value",
      backgroundColor: "rgb(255, 99, 132)",
      borderColor: "rgb(255, 99, 132)",
      data: dataLabels,
    },
  ],
};

const config = {
  type: "line",
  data: data,
  options: {
    plugins: {
      title: {
   
        display: true,
        text: "Value chart",
        font: {
          size: 20,
        },
      },
    },
  },

};
const myChart = new Chart(document.getElementById("myChart"), config);