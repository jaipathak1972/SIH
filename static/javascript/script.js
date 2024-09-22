// chart for general health
const general = document.getElementById("chart1_1").getContext("2d");

new Chart(general, {
  type: "doughnut",
  data: {
    datasets: [
      {
        label: "Water Retention",
        data: [68, 32],
        backgroundColor: ["rgba(153, 102, 255)", "rgba(201, 203, 207,0.2)"],
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      x: {
        display: false,
      },
      y: {
        display: false,
        beginAtZero: true,
      },
    },
  },
});

// chart for water balance
const water = document.getElementById("chart1_2").getContext("2d");

new Chart(water, {
  type: "doughnut",
  data: {
    datasets: [
      {
        label: "Water Retention",
        data: [75, 25],
        backgroundColor: ["rgba(255, 99, 132)", "rgba(201, 203, 207,0.2)"],
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      x: {
        display: false,
      },
      y: {
        display: false,
        beginAtZero: true,
      },
    },
  },
});

// // chart for per week score
const activity = document.getElementById("chart2");

new Chart(activity, {
  type: "bar",
  data: {
    labels: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
    datasets: [
      {
        label: "This Week Score",
        data: [25, 54, 64, 65, 12, 87, 67],
        backgroundColor: [
          "rgba(255, 99, 132)",
          "rgba(255, 159, 64)",
          "rgba(255, 205, 86)",
          "rgba(75, 192, 192)",
          "rgba(54, 162, 235)",
          "rgba(153, 102, 255)",
          "rgba(201, 203, 207)",
        ],
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});

// chart for health condition
const health_chart = document.getElementById("chart3").getContext("2d");

new Chart(health_chart, {
  type: "line",
  data: {
    labels: [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "Jun",
      "Jul",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec",
    ],
    datasets: [
      {
        label: "Health Condition Per Year",
        data: [12, 19, 3, 5, 2, 3, 15, 8, 6, 10, 7, 12],
        borderWidth: 2.5,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});
