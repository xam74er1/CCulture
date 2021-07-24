export function createCookie(cookieName: string, cookieValue: string, daysToExpire: number)
    {
        var date = new Date();
        date.setTime(date.getTime()+(daysToExpire*24*60*60*1000));
        document.cookie = cookieName + "=" + cookieValue + "; expires=" + date.toUTCString();
    }
