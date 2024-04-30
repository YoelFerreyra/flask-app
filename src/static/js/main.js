const userForm = document.querySelector("#userform");

userForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const username = userForm["username"].value;
  const email = userForm["email"].value;
  const password = userForm["password"].value;

  try {
    const response = await fetch("/api/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username,
        password,
        email,
      }),
    });
  } catch (error) {
    console.log(error);
  }

  const data = await response.json();
  console.log(data);
});

const getUsers = async () => {
  try {
    const response = await fetch("/api/users", {
      method: "GET",
    });

    if (!response.ok) {
      throw new Error("Failed to fetch data");
    }

    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.log(error);
  }
};
