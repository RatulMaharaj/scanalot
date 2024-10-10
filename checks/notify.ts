export async function sendPushNotification(message: string, url: string) {
  return await fetch("https://api.pushover.net/1/messages.json", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      token: process.env.PUSHOVER_APP_TOKEN,
      user: process.env.PUSHOVER_USER_TOKEN,
      message,
      url,
    }),
  });
}
