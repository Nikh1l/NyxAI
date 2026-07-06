import { api } from "./api";
import type { Media } from "../types/instagram";

export async function listMedia(): Promise<Media[]> {
    const { data } = await api.get("/instagram/media");
    return data;
}
