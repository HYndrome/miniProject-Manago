let date = new Date();

const renderCalender = () => {
    const viewYear = date.getFullYear();
    const viewMonth = date.getMonth();

    document.querySelector('.year').textContent = `${viewYear}`;
    document.querySelector('.month').textContent = `${viewMonth + 1}`;

    const prevLast = new Date(viewYear, viewMonth, 0);
    const thisLast = new Date(viewYear, viewMonth + 1, 0);
    // // 여기서부터
    // const firstDate = new Date(viewYear, viewMonth, 1);

    // const n_dates = [];
    // for (let d = firstDate; d <= thisLast; d.setDate(d.getDate() + 1)) {
    //     const day = d.getDate();
    //     const isOtherMonth = d.getMonth() !== viewMonth;
    //     const isToday = d.toDateString() === new Date().toDateString();
    //     const hasEvent = my_objects.some(obj => obj.date.getDate() === day);

    //     // Add the date to the dates array with a class and event flag
    //     n_dates.push({
    //         day: day,
    //         class: isOtherMonth ? 'other' : isToday ? 'today' : '',
    //         hasEvent: hasEvent
    //     });
    // }
    // // 여기까지

    const PLDate = prevLast.getDate();
    const PLDay = prevLast.getDay();

    const TLDate = thisLast.getDate();
    const TLDay = thisLast.getDay();

    const prevDates = [];
    const thisDates = [...Array(TLDate + 1).keys()].slice(1);
    const nextDates = [];

    if (PLDay !== 6) {
        for (let i = 0; i < PLDay + 1; i++) {
            prevDates.unshift(PLDate - i);
        }
    }

    for (let i = 1; i < 7 - TLDay; i++) {
        nextDates.push(i);
    }

    const dates = prevDates.concat(thisDates, nextDates);
    const firstDateIndex = dates.indexOf(1);
    const lastDateIndex = dates.lastIndexOf(TLDate);

    dates.forEach((date, i) => {
        const condition = i >= firstDateIndex && i < lastDateIndex + 1 ?
            'this' :
            'other';
            
        dates[i] = `
            <div class="date ${condition}">

                <div class="date-itm">
                    ${date}
                </div>

                <div class="date_event">
                    <div class="event-itm">EVENT</div>
                </div>

            </div>
        `;
    });

    document.querySelector('.dates').innerHTML = dates.join('');

    const today = new Date();
    if (viewMonth === today.getMonth() && viewYear === today.getFullYear()) {
        for (let date of document.querySelectorAll('.date-itm')) {
            if (+date.innerText === today.getDate()) {
                date.parentNode.classList.add('today');
                break;

            }
        }
    }
};

renderCalender();

const prevMonth = () => {
    date.setMonth(date.getMonth() - 1);
    renderCalender();
};

const nextMonth = () => {
    date.setMonth(date.getMonth() + 1);
    renderCalender();
};

const goToday = () => {
    date = new Date();
    renderCalender();
};