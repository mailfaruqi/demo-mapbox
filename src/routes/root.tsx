import { Outlet, Link } from "react-router-dom";

export function RootRoute() {
  return (
    <div>
      <header>
        <h1>
          <Link to="/">HEADER</Link>
        </h1>
      </header>

      <Outlet />

      <h1>
        <Link to="/map-marker">1. Multiple Points</Link>
      </h1>

      <footer>
        <p>COPYRIGHT</p>
      </footer>
    </div>
  );
}
