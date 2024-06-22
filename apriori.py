from typing import Set

from classes.dataset import Dataset
from classes.itemset import Itemset
from classes.itemsets_with_occurrence_counts import ItemsetsWithOccurrenceCounts


class Apriori:
    def __init__(self, min_support: int = 2):
        """
        Initialize the Apriori algorithm with the a minimum (absolute) support.

        Parameters:
        min_support (int): The minimum (absolute) support. This parameter defines the minimum number
                           of occurrences an itemset must have to be considered frequent. Must be a positive integer.
                           Default value is 2.
        """
        # Ensure that the minimum support is a positive integer
        if not isinstance(min_support, int) or min_support < 1:
            raise ValueError("The minimum support must be a positive integer.")

        self.min_support = min_support
        self.frequent_itemsets = set()

    def _generate_one_itemsets(self, dataset: Dataset) -> Set[Itemset]:

        one_itemsets= set()
        for transaction in Dataset.transactions:
            for item in transaction:
                one_itemsets.add(Itemset(frozenset([Itemset]))
         return one_itemsets                        
        """
        Generate all 1-itemsets for the given dataset.

        Parameters:
        dataset (Dataset): The dataset for which the 1-itemsets should be generated.

        Returns:
        Set[Itemset]: A set containing all 1-itemsets that are contained in the dataset.
        """
        # TODO

    def _count_occurrences_of_itemsets(
        self, dataset: Dataset, itemsets: Set[Itemset]
    ) -> ItemsetsWithOccurrenceCounts:

        ItemsetsWithOccurenceCounts={itemset: 0 for itemset in itemsets}
        for transaction in dataset.transactions:
            Transaction = frozenset(transaction)
            for itemset in itemsets:
                if itemset.issubset(Transaction):
                    ItemsetsWithOccurenceCounts[itemset]+=1
        
        return ItemsetsWithOccurenceCounts
        """
        Count the occurrences of the given itemsets in the dataset.

        Parameters:
        dataset (Dataset): The dataset for which the itemset occurrences should be counted.
        itemsets (Set[Itemset]): The itemsets for which the occurrences should be counted. The itemsets do not need to be present in the dataset.

        Returns:
        ItemsetsWithOccurrenceCounts: A dictionary containing the itemsets as keys and their occurrence counts as values.
        """
        # TODO

    def _prune_itemsets_below_min_support(
        self,
        itemsets_with_occurrence_counts: ItemsetsWithOccurrenceCounts,
    ) -> Set[Itemset]:

        pruned_itemset = {itemset for itemset,ItemsetsWithOccurenceCounts in itemsets_with_occurence_counts.items() if ItemsetsWithOccurenceCounts>= self.min_support)
        return pruned_itemset                  
        """
        Prune itemsets that are below the minimum support threshold.

        Parameters:
        itemsets_with_occurrence_counts (ItemsetsWithOccurrenceCounts): A dictionary containing the itemsets as keys and their occurrence counts as values.

        Returns:
        Set[Itemset]: A set containing all itemsets that are considered frequent.
        """
        # TODO

    def _generate_candidate_itemsets(
        self, frequent_itemsets: Set[Itemset]
    ) -> Set[Itemset]:

        candidate_itemsets=set()
        frequent_items=[itemset.items for itemset in frequent_itemsets]
        k=max(len(itemset) for itemset in frequent_items)
        
        for i in range(len(frequent_items)):
            for j in range(i+1,len(frequent_items)):
                union_items=frequent_items[i].union(frequent_items[j])
                if len(union_items)==k+1:
                    candidate_itemsets.add(Itemset(union_items))
                    
        return candidate_itemsets
        """
        Generate length-k+1 candidate itemsets based on the given frequent itemsets. k is the length of the longest frequent itemset.

        Parameters:
        frequent_itemsets (Set[Itemset]): A set containing all frequent itemsets.

        Returns:
        Set[Itemset]: A set containing all length-k+1 candidate itemsets.
        """
        # If there are no frequent itemsets, return an empty set
        if not frequent_itemsets:
            return set()

        # TODO

    def fit(self, dataset: Dataset):
        self._init_(dataset)
        one_itemset= self._generate_one_itemset(dataset)
        while itemset:
            itemset_occurences_counts= self._count_occurrences_of_itemsets( dataset, itemset)
            frequent_itemsets= self._prune_itemsets_below_min_support(itemset_occurences_counts)
            self.frequent_itemsets.update(frequent_itemsets)
            candidate_itemsets= self._generate_candidate_itemsets(frequent_itemsets)
        """
        Use the Apriori algorithm to find all frequent itemsets in the given dataset.
        Saves the frequent itemsets in the frequent_itemsets attribute.

        Parameters:
        dataset (Dataset): The dataset to which the Apriori algorithm should be fitted.
        """
        # Reset the set of frequent itemsets
        self.frequent_itemsets = set()

        # TODO
