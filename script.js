const stationDistances = {
  CHN: 0, SLM: 350, BLR: 550, KRN: 900, HYB: 1200,
  NGP: 1600, ITJ: 1900, BPL: 2000, AGA: 2500,
  NJP: 2700, PTA: 3800, GHY: 4000
};

function isValidStation(st) {
  return stationDistances.hasOwnProperty(st);
}

function getFilteredSortedBogies(bogies) {
  return bogies.filter(b => stationDistances[b] > stationDistances["HYB"])
               .sort((a, b) => stationDistances[b] - stationDistances[a]);
}

function renderTrain(lineId, title, bogies) {
  const container = document.getElementById(lineId);
  container.innerHTML = `<h3>${title}</h3><div class="train-line">`;

  if (bogies[0] === "JOURNEY_ENDED") {
    container.innerHTML += `<p style="color:red;">JOURNEY_ENDED</p>`;
    return;
  }

  bogies.forEach((b, idx) => {
    if (idx > 0) container.innerHTML += `<div class="arrow">➔</div>`;
    container.innerHTML += `<div class="bogie ${b === "ENGINE" ? 'engine' : ''}">
      ${b === "ENGINE" ? "🚂 ENGINE" : `🚃 ${b}`}
    </div>`;
  });

  container.innerHTML += `</div>`;
}

function mergeTrains() {
  const trainA = document.getElementById("trainA").value.trim().split(" ").filter(isValidStation);
  const trainB = document.getElementById("trainB").value.trim().split(" ").filter(isValidStation);

  const aAfterHYB = getFilteredSortedBogies(trainA);
  const bAfterHYB = getFilteredSortedBogies(trainB.reverse());

  const arrivalA = ["ENGINE", ...aAfterHYB];
  const arrivalB = ["ENGINE", ...bAfterHYB];

  let departure = [];
  if (aAfterHYB.length === 0 && bAfterHYB.length === 0) {
    departure = ["JOURNEY_ENDED"];
  } else {
    departure = ["ENGINE", "ENGINE", ...bAfterHYB, ...aAfterHYB];
  }

  renderTrain("arrivalA", "ARRIVAL TRAIN_A", arrivalA);
  renderTrain("arrivalB", "ARRIVAL TRAIN_B", arrivalB);
  renderTrain("departureAB", "DEPARTURE TRAIN_AB", departure);
}
