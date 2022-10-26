const url_container = $("#url_container");
const url_container_first = $("#url_container_first");
const sensor_container = $("#sensor_container");

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
      let row = table.insertRow();
      let id = row.insertCell(0);
      id.innerHTML = val.id;
      let value = row.insertCell(1);
      value.innerHTML = val.value;
      let arduino_date = row.insertCell(2);
      arduino_date.innerHTML = val.arduino_date;
      let server_date = row.insertCell(3);
      server_date.innerHTML = val.server_date;
      chartLabels.push(val.arduino_date.replace("T", " ").split(".")[0]);
      dataLabels.push(val.value);
    });
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
