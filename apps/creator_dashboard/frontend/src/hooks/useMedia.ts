import { useQuery } from "@tanstack/react-query";
import { listMedia } from "../services/instagram";

export function useMedia() {
    return useQuery({
        queryKey: ["media"],
        queryFn: listMedia
    });
}
