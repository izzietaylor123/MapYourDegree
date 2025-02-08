import './Home.css'
import Header from "./Header";

export default function Home() {
	return (
		<div>
			<Header />
		</div>
	);
}

// Header.tsx
export function Header() {
	return (
		<h2>Map Your Degree</h2>
	);
}