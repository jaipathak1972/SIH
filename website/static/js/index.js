//function for sidebar
const links = document.querySelectorAll('.sidebar a');

links.forEach(link => {
  link.addEventListener('click', function() {
    links.forEach(l => l.classList.remove('active'));
    this.classList.add('active');
  });
});

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
  responsive:true,
    scales: { 
      y: {
        beginAtZero: true,
      },
    },
  },
});

const currentDate = new Date();
const monthNames = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];
const daysInMonth = new Date(
  currentDate.getFullYear(),
  currentDate.getMonth() + 1,
  0
).getDate(); // Get number of days in the current month
const firstDayIndex = new Date(
  currentDate.getFullYear(),
  currentDate.getMonth(),
  1
).getDay(); // Get the day of the week the month starts on

// Set the header to the current month and year
document.getElementById("calendarMonthYear").textContent =
  monthNames[currentDate.getMonth()] + " " + currentDate.getFullYear();

const calendarDays = document.querySelector(".calendar_days");

// Add empty spaces for days before the first day of the month
for (let i = 0; i < firstDayIndex; i++) {
  const emptyCell = document.createElement("div");
  emptyCell.classList.add("day");
  calendarDays.appendChild(emptyCell);
}

// Add the actual days of the month
for (let i = 1; i <= daysInMonth; i++) {
  const dayCell = document.createElement("div");
  dayCell.classList.add("day", "day_number");
  dayCell.textContent = i;

  if (i === currentDate.getDate()) {
            dayCell.classList.add('current_day');
        }

  calendarDays.appendChild(dayCell);
}