import { QueryClient } from "@tanstack/react-query";
import { QueryClientProvider } from "@tanstack/react-query";

import Dashboard from "./pages/Dashboard";

const queryClient = new QueryClient();

export default function App() {

    return (

        <QueryClientProvider client={queryClient}>

            <Dashboard />

        </QueryClientProvider>

    );
}