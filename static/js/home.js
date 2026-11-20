document.addEventListener("DOMContentLoaded", function () {
  const tripOptions = document.querySelectorAll('input[name="trip_type_ui"]');
  const tripTypeInput = document.getElementById("tripType");
  const returnWrap = document.querySelector(".return-date-wrap");
  const returnDate = document.getElementById("returnDate");
  const departureDate = document.getElementById("departureDate");

  // تاریخ رفت از امروز زودتر انتخاب نشود.
  const today = new Date();
  const localToday = new Date(today.getTime() - today.getTimezoneOffset() * 60000)
    .toISOString().split("T")[0];
  departureDate.min = localToday;
  returnDate.min = localToday;

  departureDate.addEventListener("change", function () {
    returnDate.min = departureDate.value || localToday;
    if (returnDate.value && returnDate.value < departureDate.value) {
      returnDate.value = "";
    }
  });

  tripOptions.forEach(function (option) {
    option.addEventListener("change", function () {
      document.querySelectorAll(".trip-option").forEach(el => el.classList.remove("active"));
      option.closest(".trip-option").classList.add("active");

      const isRoundTrip = option.value === "round_trip";
      tripTypeInput.value = option.value;
      returnWrap.classList.toggle("d-none", !isRoundTrip);
      returnDate.required = isRoundTrip;
      if (!isRoundTrip) returnDate.value = "";
    });
  });

  // جلوگیری از انتخاب مقصد و مبدأ یکسان در فرم نمایشی.
  document.getElementById("flightSearchForm").addEventListener("submit", function (event) {
    const origin = document.getElementById("origin").value.trim().toLowerCase();
    const destination = document.getElementById("destination").value.trim().toLowerCase();
    if (origin && destination && origin === destination) {
      event.preventDefault();
      alert("مبدأ و مقصد نمی‌توانند یکسان باشند.");
    }
  });
});
